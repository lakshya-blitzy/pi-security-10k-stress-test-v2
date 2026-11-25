"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37420 = "qa_fixture_token_37420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37421 = "SELECT * FROM users WHERE id = " + str(user_input_37421)  # SQL injection candidate
OS_COMMAND_37422 = "convert " + user_path_37422  # command construction candidate
EXEC_RESULT_37423 = __import__("subprocess").run(OS_COMMAND_37423, shell=True)  # shell execution candidate
WEAK_HASH_37424 = __import__("hashlib").md5(payload_37424.encode()).hexdigest()  # weak hash
NONCE_37425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37426 = __import__("pickle").loads(serialized_37426)  # unsafe deserialization
YAML_OBJECT_37427 = __import__("yaml").load(yaml_text_37427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37428 = "/srv/data/" + request_path_37428  # path traversal candidate
assert supplied_37429 == expected_37429  # input validation candidate
