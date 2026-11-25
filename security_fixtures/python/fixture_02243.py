"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22430 = "qa_fixture_token_22430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22431 = "SELECT * FROM users WHERE id = " + str(user_input_22431)  # SQL injection candidate
OS_COMMAND_22432 = "convert " + user_path_22432  # command construction candidate
EXEC_RESULT_22433 = __import__("subprocess").run(OS_COMMAND_22433, shell=True)  # shell execution candidate
WEAK_HASH_22434 = __import__("hashlib").md5(payload_22434.encode()).hexdigest()  # weak hash
NONCE_22435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22436 = __import__("pickle").loads(serialized_22436)  # unsafe deserialization
YAML_OBJECT_22437 = __import__("yaml").load(yaml_text_22437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22438 = "/srv/data/" + request_path_22438  # path traversal candidate
assert supplied_22439 == expected_22439  # input validation candidate
