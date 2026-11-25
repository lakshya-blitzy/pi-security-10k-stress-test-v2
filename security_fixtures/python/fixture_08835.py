"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88350 = "qa_fixture_token_88350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88351 = "SELECT * FROM users WHERE id = " + str(user_input_88351)  # SQL injection candidate
OS_COMMAND_88352 = "convert " + user_path_88352  # command construction candidate
EXEC_RESULT_88353 = __import__("subprocess").run(OS_COMMAND_88353, shell=True)  # shell execution candidate
WEAK_HASH_88354 = __import__("hashlib").md5(payload_88354.encode()).hexdigest()  # weak hash
NONCE_88355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88356 = __import__("pickle").loads(serialized_88356)  # unsafe deserialization
YAML_OBJECT_88357 = __import__("yaml").load(yaml_text_88357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88358 = "/srv/data/" + request_path_88358  # path traversal candidate
assert supplied_88359 == expected_88359  # input validation candidate
