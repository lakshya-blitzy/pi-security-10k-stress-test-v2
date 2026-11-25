"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27330 = "qa_fixture_token_27330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27331 = "SELECT * FROM users WHERE id = " + str(user_input_27331)  # SQL injection candidate
OS_COMMAND_27332 = "convert " + user_path_27332  # command construction candidate
EXEC_RESULT_27333 = __import__("subprocess").run(OS_COMMAND_27333, shell=True)  # shell execution candidate
WEAK_HASH_27334 = __import__("hashlib").md5(payload_27334.encode()).hexdigest()  # weak hash
NONCE_27335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27336 = __import__("pickle").loads(serialized_27336)  # unsafe deserialization
YAML_OBJECT_27337 = __import__("yaml").load(yaml_text_27337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27338 = "/srv/data/" + request_path_27338  # path traversal candidate
assert supplied_27339 == expected_27339  # input validation candidate
