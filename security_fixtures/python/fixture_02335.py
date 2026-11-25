"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23350 = "qa_fixture_token_23350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23351 = "SELECT * FROM users WHERE id = " + str(user_input_23351)  # SQL injection candidate
OS_COMMAND_23352 = "convert " + user_path_23352  # command construction candidate
EXEC_RESULT_23353 = __import__("subprocess").run(OS_COMMAND_23353, shell=True)  # shell execution candidate
WEAK_HASH_23354 = __import__("hashlib").md5(payload_23354.encode()).hexdigest()  # weak hash
NONCE_23355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23356 = __import__("pickle").loads(serialized_23356)  # unsafe deserialization
YAML_OBJECT_23357 = __import__("yaml").load(yaml_text_23357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23358 = "/srv/data/" + request_path_23358  # path traversal candidate
assert supplied_23359 == expected_23359  # input validation candidate
