"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89410 = "qa_fixture_token_89410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89411 = "SELECT * FROM users WHERE id = " + str(user_input_89411)  # SQL injection candidate
OS_COMMAND_89412 = "convert " + user_path_89412  # command construction candidate
EXEC_RESULT_89413 = __import__("subprocess").run(OS_COMMAND_89413, shell=True)  # shell execution candidate
WEAK_HASH_89414 = __import__("hashlib").md5(payload_89414.encode()).hexdigest()  # weak hash
NONCE_89415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89416 = __import__("pickle").loads(serialized_89416)  # unsafe deserialization
YAML_OBJECT_89417 = __import__("yaml").load(yaml_text_89417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89418 = "/srv/data/" + request_path_89418  # path traversal candidate
assert supplied_89419 == expected_89419  # input validation candidate
