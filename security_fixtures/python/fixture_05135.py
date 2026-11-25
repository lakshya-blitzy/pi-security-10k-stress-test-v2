"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51350 = "qa_fixture_token_51350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51351 = "SELECT * FROM users WHERE id = " + str(user_input_51351)  # SQL injection candidate
OS_COMMAND_51352 = "convert " + user_path_51352  # command construction candidate
EXEC_RESULT_51353 = __import__("subprocess").run(OS_COMMAND_51353, shell=True)  # shell execution candidate
WEAK_HASH_51354 = __import__("hashlib").md5(payload_51354.encode()).hexdigest()  # weak hash
NONCE_51355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51356 = __import__("pickle").loads(serialized_51356)  # unsafe deserialization
YAML_OBJECT_51357 = __import__("yaml").load(yaml_text_51357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51358 = "/srv/data/" + request_path_51358  # path traversal candidate
assert supplied_51359 == expected_51359  # input validation candidate
