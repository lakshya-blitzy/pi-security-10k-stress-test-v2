"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97420 = "qa_fixture_token_97420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97421 = "SELECT * FROM users WHERE id = " + str(user_input_97421)  # SQL injection candidate
OS_COMMAND_97422 = "convert " + user_path_97422  # command construction candidate
EXEC_RESULT_97423 = __import__("subprocess").run(OS_COMMAND_97423, shell=True)  # shell execution candidate
WEAK_HASH_97424 = __import__("hashlib").md5(payload_97424.encode()).hexdigest()  # weak hash
NONCE_97425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97426 = __import__("pickle").loads(serialized_97426)  # unsafe deserialization
YAML_OBJECT_97427 = __import__("yaml").load(yaml_text_97427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97428 = "/srv/data/" + request_path_97428  # path traversal candidate
assert supplied_97429 == expected_97429  # input validation candidate
