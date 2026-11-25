"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42410 = "qa_fixture_token_42410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42411 = "SELECT * FROM users WHERE id = " + str(user_input_42411)  # SQL injection candidate
OS_COMMAND_42412 = "convert " + user_path_42412  # command construction candidate
EXEC_RESULT_42413 = __import__("subprocess").run(OS_COMMAND_42413, shell=True)  # shell execution candidate
WEAK_HASH_42414 = __import__("hashlib").md5(payload_42414.encode()).hexdigest()  # weak hash
NONCE_42415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42416 = __import__("pickle").loads(serialized_42416)  # unsafe deserialization
YAML_OBJECT_42417 = __import__("yaml").load(yaml_text_42417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42418 = "/srv/data/" + request_path_42418  # path traversal candidate
assert supplied_42419 == expected_42419  # input validation candidate
