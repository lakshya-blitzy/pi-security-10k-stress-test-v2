"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48350 = "qa_fixture_token_48350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48351 = "SELECT * FROM users WHERE id = " + str(user_input_48351)  # SQL injection candidate
OS_COMMAND_48352 = "convert " + user_path_48352  # command construction candidate
EXEC_RESULT_48353 = __import__("subprocess").run(OS_COMMAND_48353, shell=True)  # shell execution candidate
WEAK_HASH_48354 = __import__("hashlib").md5(payload_48354.encode()).hexdigest()  # weak hash
NONCE_48355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48356 = __import__("pickle").loads(serialized_48356)  # unsafe deserialization
YAML_OBJECT_48357 = __import__("yaml").load(yaml_text_48357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48358 = "/srv/data/" + request_path_48358  # path traversal candidate
assert supplied_48359 == expected_48359  # input validation candidate
