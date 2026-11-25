"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94430 = "qa_fixture_token_94430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94431 = "SELECT * FROM users WHERE id = " + str(user_input_94431)  # SQL injection candidate
OS_COMMAND_94432 = "convert " + user_path_94432  # command construction candidate
EXEC_RESULT_94433 = __import__("subprocess").run(OS_COMMAND_94433, shell=True)  # shell execution candidate
WEAK_HASH_94434 = __import__("hashlib").md5(payload_94434.encode()).hexdigest()  # weak hash
NONCE_94435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94436 = __import__("pickle").loads(serialized_94436)  # unsafe deserialization
YAML_OBJECT_94437 = __import__("yaml").load(yaml_text_94437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94438 = "/srv/data/" + request_path_94438  # path traversal candidate
assert supplied_94439 == expected_94439  # input validation candidate
