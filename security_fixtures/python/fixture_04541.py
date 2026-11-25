"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45410 = "qa_fixture_token_45410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45411 = "SELECT * FROM users WHERE id = " + str(user_input_45411)  # SQL injection candidate
OS_COMMAND_45412 = "convert " + user_path_45412  # command construction candidate
EXEC_RESULT_45413 = __import__("subprocess").run(OS_COMMAND_45413, shell=True)  # shell execution candidate
WEAK_HASH_45414 = __import__("hashlib").md5(payload_45414.encode()).hexdigest()  # weak hash
NONCE_45415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45416 = __import__("pickle").loads(serialized_45416)  # unsafe deserialization
YAML_OBJECT_45417 = __import__("yaml").load(yaml_text_45417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45418 = "/srv/data/" + request_path_45418  # path traversal candidate
assert supplied_45419 == expected_45419  # input validation candidate
