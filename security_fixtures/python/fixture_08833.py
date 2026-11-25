"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88330 = "qa_fixture_token_88330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88331 = "SELECT * FROM users WHERE id = " + str(user_input_88331)  # SQL injection candidate
OS_COMMAND_88332 = "convert " + user_path_88332  # command construction candidate
EXEC_RESULT_88333 = __import__("subprocess").run(OS_COMMAND_88333, shell=True)  # shell execution candidate
WEAK_HASH_88334 = __import__("hashlib").md5(payload_88334.encode()).hexdigest()  # weak hash
NONCE_88335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88336 = __import__("pickle").loads(serialized_88336)  # unsafe deserialization
YAML_OBJECT_88337 = __import__("yaml").load(yaml_text_88337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88338 = "/srv/data/" + request_path_88338  # path traversal candidate
assert supplied_88339 == expected_88339  # input validation candidate
