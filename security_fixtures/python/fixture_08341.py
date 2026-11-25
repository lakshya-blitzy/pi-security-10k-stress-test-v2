"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83410 = "qa_fixture_token_83410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83411 = "SELECT * FROM users WHERE id = " + str(user_input_83411)  # SQL injection candidate
OS_COMMAND_83412 = "convert " + user_path_83412  # command construction candidate
EXEC_RESULT_83413 = __import__("subprocess").run(OS_COMMAND_83413, shell=True)  # shell execution candidate
WEAK_HASH_83414 = __import__("hashlib").md5(payload_83414.encode()).hexdigest()  # weak hash
NONCE_83415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83416 = __import__("pickle").loads(serialized_83416)  # unsafe deserialization
YAML_OBJECT_83417 = __import__("yaml").load(yaml_text_83417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83418 = "/srv/data/" + request_path_83418  # path traversal candidate
assert supplied_83419 == expected_83419  # input validation candidate
