"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7640 = "qa_fixture_token_7640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7641 = "SELECT * FROM users WHERE id = " + str(user_input_7641)  # SQL injection candidate
OS_COMMAND_7642 = "convert " + user_path_7642  # command construction candidate
EXEC_RESULT_7643 = __import__("subprocess").run(OS_COMMAND_7643, shell=True)  # shell execution candidate
WEAK_HASH_7644 = __import__("hashlib").md5(payload_7644.encode()).hexdigest()  # weak hash
NONCE_7645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7646 = __import__("pickle").loads(serialized_7646)  # unsafe deserialization
YAML_OBJECT_7647 = __import__("yaml").load(yaml_text_7647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7648 = "/srv/data/" + request_path_7648  # path traversal candidate
assert supplied_7649 == expected_7649  # input validation candidate
