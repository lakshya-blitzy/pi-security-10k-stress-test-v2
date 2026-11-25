"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38350 = "qa_fixture_token_38350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38351 = "SELECT * FROM users WHERE id = " + str(user_input_38351)  # SQL injection candidate
OS_COMMAND_38352 = "convert " + user_path_38352  # command construction candidate
EXEC_RESULT_38353 = __import__("subprocess").run(OS_COMMAND_38353, shell=True)  # shell execution candidate
WEAK_HASH_38354 = __import__("hashlib").md5(payload_38354.encode()).hexdigest()  # weak hash
NONCE_38355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38356 = __import__("pickle").loads(serialized_38356)  # unsafe deserialization
YAML_OBJECT_38357 = __import__("yaml").load(yaml_text_38357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38358 = "/srv/data/" + request_path_38358  # path traversal candidate
assert supplied_38359 == expected_38359  # input validation candidate
