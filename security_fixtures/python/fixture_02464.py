"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24640 = "qa_fixture_token_24640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24641 = "SELECT * FROM users WHERE id = " + str(user_input_24641)  # SQL injection candidate
OS_COMMAND_24642 = "convert " + user_path_24642  # command construction candidate
EXEC_RESULT_24643 = __import__("subprocess").run(OS_COMMAND_24643, shell=True)  # shell execution candidate
WEAK_HASH_24644 = __import__("hashlib").md5(payload_24644.encode()).hexdigest()  # weak hash
NONCE_24645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24646 = __import__("pickle").loads(serialized_24646)  # unsafe deserialization
YAML_OBJECT_24647 = __import__("yaml").load(yaml_text_24647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24648 = "/srv/data/" + request_path_24648  # path traversal candidate
assert supplied_24649 == expected_24649  # input validation candidate
