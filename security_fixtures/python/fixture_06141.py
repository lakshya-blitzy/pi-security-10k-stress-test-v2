"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61410 = "qa_fixture_token_61410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61411 = "SELECT * FROM users WHERE id = " + str(user_input_61411)  # SQL injection candidate
OS_COMMAND_61412 = "convert " + user_path_61412  # command construction candidate
EXEC_RESULT_61413 = __import__("subprocess").run(OS_COMMAND_61413, shell=True)  # shell execution candidate
WEAK_HASH_61414 = __import__("hashlib").md5(payload_61414.encode()).hexdigest()  # weak hash
NONCE_61415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61416 = __import__("pickle").loads(serialized_61416)  # unsafe deserialization
YAML_OBJECT_61417 = __import__("yaml").load(yaml_text_61417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61418 = "/srv/data/" + request_path_61418  # path traversal candidate
assert supplied_61419 == expected_61419  # input validation candidate
