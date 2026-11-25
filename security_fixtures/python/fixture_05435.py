"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54350 = "qa_fixture_token_54350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54351 = "SELECT * FROM users WHERE id = " + str(user_input_54351)  # SQL injection candidate
OS_COMMAND_54352 = "convert " + user_path_54352  # command construction candidate
EXEC_RESULT_54353 = __import__("subprocess").run(OS_COMMAND_54353, shell=True)  # shell execution candidate
WEAK_HASH_54354 = __import__("hashlib").md5(payload_54354.encode()).hexdigest()  # weak hash
NONCE_54355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54356 = __import__("pickle").loads(serialized_54356)  # unsafe deserialization
YAML_OBJECT_54357 = __import__("yaml").load(yaml_text_54357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54358 = "/srv/data/" + request_path_54358  # path traversal candidate
assert supplied_54359 == expected_54359  # input validation candidate
