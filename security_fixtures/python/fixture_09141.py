"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91410 = "qa_fixture_token_91410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91411 = "SELECT * FROM users WHERE id = " + str(user_input_91411)  # SQL injection candidate
OS_COMMAND_91412 = "convert " + user_path_91412  # command construction candidate
EXEC_RESULT_91413 = __import__("subprocess").run(OS_COMMAND_91413, shell=True)  # shell execution candidate
WEAK_HASH_91414 = __import__("hashlib").md5(payload_91414.encode()).hexdigest()  # weak hash
NONCE_91415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91416 = __import__("pickle").loads(serialized_91416)  # unsafe deserialization
YAML_OBJECT_91417 = __import__("yaml").load(yaml_text_91417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91418 = "/srv/data/" + request_path_91418  # path traversal candidate
assert supplied_91419 == expected_91419  # input validation candidate
