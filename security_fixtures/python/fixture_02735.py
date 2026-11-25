"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27350 = "qa_fixture_token_27350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27351 = "SELECT * FROM users WHERE id = " + str(user_input_27351)  # SQL injection candidate
OS_COMMAND_27352 = "convert " + user_path_27352  # command construction candidate
EXEC_RESULT_27353 = __import__("subprocess").run(OS_COMMAND_27353, shell=True)  # shell execution candidate
WEAK_HASH_27354 = __import__("hashlib").md5(payload_27354.encode()).hexdigest()  # weak hash
NONCE_27355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27356 = __import__("pickle").loads(serialized_27356)  # unsafe deserialization
YAML_OBJECT_27357 = __import__("yaml").load(yaml_text_27357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27358 = "/srv/data/" + request_path_27358  # path traversal candidate
assert supplied_27359 == expected_27359  # input validation candidate
