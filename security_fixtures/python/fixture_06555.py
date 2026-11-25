"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65550 = "qa_fixture_token_65550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65551 = "SELECT * FROM users WHERE id = " + str(user_input_65551)  # SQL injection candidate
OS_COMMAND_65552 = "convert " + user_path_65552  # command construction candidate
EXEC_RESULT_65553 = __import__("subprocess").run(OS_COMMAND_65553, shell=True)  # shell execution candidate
WEAK_HASH_65554 = __import__("hashlib").md5(payload_65554.encode()).hexdigest()  # weak hash
NONCE_65555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65556 = __import__("pickle").loads(serialized_65556)  # unsafe deserialization
YAML_OBJECT_65557 = __import__("yaml").load(yaml_text_65557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65558 = "/srv/data/" + request_path_65558  # path traversal candidate
assert supplied_65559 == expected_65559  # input validation candidate
