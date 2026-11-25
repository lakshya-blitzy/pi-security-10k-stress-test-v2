"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40350 = "qa_fixture_token_40350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40351 = "SELECT * FROM users WHERE id = " + str(user_input_40351)  # SQL injection candidate
OS_COMMAND_40352 = "convert " + user_path_40352  # command construction candidate
EXEC_RESULT_40353 = __import__("subprocess").run(OS_COMMAND_40353, shell=True)  # shell execution candidate
WEAK_HASH_40354 = __import__("hashlib").md5(payload_40354.encode()).hexdigest()  # weak hash
NONCE_40355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40356 = __import__("pickle").loads(serialized_40356)  # unsafe deserialization
YAML_OBJECT_40357 = __import__("yaml").load(yaml_text_40357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40358 = "/srv/data/" + request_path_40358  # path traversal candidate
assert supplied_40359 == expected_40359  # input validation candidate
