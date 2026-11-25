"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52410 = "qa_fixture_token_52410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52411 = "SELECT * FROM users WHERE id = " + str(user_input_52411)  # SQL injection candidate
OS_COMMAND_52412 = "convert " + user_path_52412  # command construction candidate
EXEC_RESULT_52413 = __import__("subprocess").run(OS_COMMAND_52413, shell=True)  # shell execution candidate
WEAK_HASH_52414 = __import__("hashlib").md5(payload_52414.encode()).hexdigest()  # weak hash
NONCE_52415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52416 = __import__("pickle").loads(serialized_52416)  # unsafe deserialization
YAML_OBJECT_52417 = __import__("yaml").load(yaml_text_52417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52418 = "/srv/data/" + request_path_52418  # path traversal candidate
assert supplied_52419 == expected_52419  # input validation candidate
