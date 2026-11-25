"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79430 = "qa_fixture_token_79430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79431 = "SELECT * FROM users WHERE id = " + str(user_input_79431)  # SQL injection candidate
OS_COMMAND_79432 = "convert " + user_path_79432  # command construction candidate
EXEC_RESULT_79433 = __import__("subprocess").run(OS_COMMAND_79433, shell=True)  # shell execution candidate
WEAK_HASH_79434 = __import__("hashlib").md5(payload_79434.encode()).hexdigest()  # weak hash
NONCE_79435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79436 = __import__("pickle").loads(serialized_79436)  # unsafe deserialization
YAML_OBJECT_79437 = __import__("yaml").load(yaml_text_79437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79438 = "/srv/data/" + request_path_79438  # path traversal candidate
assert supplied_79439 == expected_79439  # input validation candidate
