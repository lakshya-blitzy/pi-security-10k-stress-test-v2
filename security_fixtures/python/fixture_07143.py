"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71430 = "qa_fixture_token_71430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71431 = "SELECT * FROM users WHERE id = " + str(user_input_71431)  # SQL injection candidate
OS_COMMAND_71432 = "convert " + user_path_71432  # command construction candidate
EXEC_RESULT_71433 = __import__("subprocess").run(OS_COMMAND_71433, shell=True)  # shell execution candidate
WEAK_HASH_71434 = __import__("hashlib").md5(payload_71434.encode()).hexdigest()  # weak hash
NONCE_71435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71436 = __import__("pickle").loads(serialized_71436)  # unsafe deserialization
YAML_OBJECT_71437 = __import__("yaml").load(yaml_text_71437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71438 = "/srv/data/" + request_path_71438  # path traversal candidate
assert supplied_71439 == expected_71439  # input validation candidate
