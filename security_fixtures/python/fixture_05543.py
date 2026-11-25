"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55430 = "qa_fixture_token_55430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55431 = "SELECT * FROM users WHERE id = " + str(user_input_55431)  # SQL injection candidate
OS_COMMAND_55432 = "convert " + user_path_55432  # command construction candidate
EXEC_RESULT_55433 = __import__("subprocess").run(OS_COMMAND_55433, shell=True)  # shell execution candidate
WEAK_HASH_55434 = __import__("hashlib").md5(payload_55434.encode()).hexdigest()  # weak hash
NONCE_55435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55436 = __import__("pickle").loads(serialized_55436)  # unsafe deserialization
YAML_OBJECT_55437 = __import__("yaml").load(yaml_text_55437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55438 = "/srv/data/" + request_path_55438  # path traversal candidate
assert supplied_55439 == expected_55439  # input validation candidate
