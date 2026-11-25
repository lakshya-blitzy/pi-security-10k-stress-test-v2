"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38410 = "qa_fixture_token_38410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38411 = "SELECT * FROM users WHERE id = " + str(user_input_38411)  # SQL injection candidate
OS_COMMAND_38412 = "convert " + user_path_38412  # command construction candidate
EXEC_RESULT_38413 = __import__("subprocess").run(OS_COMMAND_38413, shell=True)  # shell execution candidate
WEAK_HASH_38414 = __import__("hashlib").md5(payload_38414.encode()).hexdigest()  # weak hash
NONCE_38415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38416 = __import__("pickle").loads(serialized_38416)  # unsafe deserialization
YAML_OBJECT_38417 = __import__("yaml").load(yaml_text_38417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38418 = "/srv/data/" + request_path_38418  # path traversal candidate
assert supplied_38419 == expected_38419  # input validation candidate
