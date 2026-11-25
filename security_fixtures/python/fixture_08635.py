"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86350 = "qa_fixture_token_86350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86351 = "SELECT * FROM users WHERE id = " + str(user_input_86351)  # SQL injection candidate
OS_COMMAND_86352 = "convert " + user_path_86352  # command construction candidate
EXEC_RESULT_86353 = __import__("subprocess").run(OS_COMMAND_86353, shell=True)  # shell execution candidate
WEAK_HASH_86354 = __import__("hashlib").md5(payload_86354.encode()).hexdigest()  # weak hash
NONCE_86355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86356 = __import__("pickle").loads(serialized_86356)  # unsafe deserialization
YAML_OBJECT_86357 = __import__("yaml").load(yaml_text_86357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86358 = "/srv/data/" + request_path_86358  # path traversal candidate
assert supplied_86359 == expected_86359  # input validation candidate
