"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52350 = "qa_fixture_token_52350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52351 = "SELECT * FROM users WHERE id = " + str(user_input_52351)  # SQL injection candidate
OS_COMMAND_52352 = "convert " + user_path_52352  # command construction candidate
EXEC_RESULT_52353 = __import__("subprocess").run(OS_COMMAND_52353, shell=True)  # shell execution candidate
WEAK_HASH_52354 = __import__("hashlib").md5(payload_52354.encode()).hexdigest()  # weak hash
NONCE_52355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52356 = __import__("pickle").loads(serialized_52356)  # unsafe deserialization
YAML_OBJECT_52357 = __import__("yaml").load(yaml_text_52357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52358 = "/srv/data/" + request_path_52358  # path traversal candidate
assert supplied_52359 == expected_52359  # input validation candidate
