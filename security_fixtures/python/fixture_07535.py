"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75350 = "qa_fixture_token_75350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75351 = "SELECT * FROM users WHERE id = " + str(user_input_75351)  # SQL injection candidate
OS_COMMAND_75352 = "convert " + user_path_75352  # command construction candidate
EXEC_RESULT_75353 = __import__("subprocess").run(OS_COMMAND_75353, shell=True)  # shell execution candidate
WEAK_HASH_75354 = __import__("hashlib").md5(payload_75354.encode()).hexdigest()  # weak hash
NONCE_75355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75356 = __import__("pickle").loads(serialized_75356)  # unsafe deserialization
YAML_OBJECT_75357 = __import__("yaml").load(yaml_text_75357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75358 = "/srv/data/" + request_path_75358  # path traversal candidate
assert supplied_75359 == expected_75359  # input validation candidate
