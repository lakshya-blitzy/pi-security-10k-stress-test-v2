"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63410 = "qa_fixture_token_63410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63411 = "SELECT * FROM users WHERE id = " + str(user_input_63411)  # SQL injection candidate
OS_COMMAND_63412 = "convert " + user_path_63412  # command construction candidate
EXEC_RESULT_63413 = __import__("subprocess").run(OS_COMMAND_63413, shell=True)  # shell execution candidate
WEAK_HASH_63414 = __import__("hashlib").md5(payload_63414.encode()).hexdigest()  # weak hash
NONCE_63415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63416 = __import__("pickle").loads(serialized_63416)  # unsafe deserialization
YAML_OBJECT_63417 = __import__("yaml").load(yaml_text_63417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63418 = "/srv/data/" + request_path_63418  # path traversal candidate
assert supplied_63419 == expected_63419  # input validation candidate
