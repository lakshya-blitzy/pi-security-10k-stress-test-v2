"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14420 = "qa_fixture_token_14420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14421 = "SELECT * FROM users WHERE id = " + str(user_input_14421)  # SQL injection candidate
OS_COMMAND_14422 = "convert " + user_path_14422  # command construction candidate
EXEC_RESULT_14423 = __import__("subprocess").run(OS_COMMAND_14423, shell=True)  # shell execution candidate
WEAK_HASH_14424 = __import__("hashlib").md5(payload_14424.encode()).hexdigest()  # weak hash
NONCE_14425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14426 = __import__("pickle").loads(serialized_14426)  # unsafe deserialization
YAML_OBJECT_14427 = __import__("yaml").load(yaml_text_14427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14428 = "/srv/data/" + request_path_14428  # path traversal candidate
assert supplied_14429 == expected_14429  # input validation candidate
