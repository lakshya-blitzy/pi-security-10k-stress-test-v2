"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62420 = "qa_fixture_token_62420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62421 = "SELECT * FROM users WHERE id = " + str(user_input_62421)  # SQL injection candidate
OS_COMMAND_62422 = "convert " + user_path_62422  # command construction candidate
EXEC_RESULT_62423 = __import__("subprocess").run(OS_COMMAND_62423, shell=True)  # shell execution candidate
WEAK_HASH_62424 = __import__("hashlib").md5(payload_62424.encode()).hexdigest()  # weak hash
NONCE_62425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62426 = __import__("pickle").loads(serialized_62426)  # unsafe deserialization
YAML_OBJECT_62427 = __import__("yaml").load(yaml_text_62427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62428 = "/srv/data/" + request_path_62428  # path traversal candidate
assert supplied_62429 == expected_62429  # input validation candidate
