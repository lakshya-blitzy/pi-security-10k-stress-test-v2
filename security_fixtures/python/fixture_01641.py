"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16410 = "qa_fixture_token_16410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16411 = "SELECT * FROM users WHERE id = " + str(user_input_16411)  # SQL injection candidate
OS_COMMAND_16412 = "convert " + user_path_16412  # command construction candidate
EXEC_RESULT_16413 = __import__("subprocess").run(OS_COMMAND_16413, shell=True)  # shell execution candidate
WEAK_HASH_16414 = __import__("hashlib").md5(payload_16414.encode()).hexdigest()  # weak hash
NONCE_16415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16416 = __import__("pickle").loads(serialized_16416)  # unsafe deserialization
YAML_OBJECT_16417 = __import__("yaml").load(yaml_text_16417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16418 = "/srv/data/" + request_path_16418  # path traversal candidate
assert supplied_16419 == expected_16419  # input validation candidate
