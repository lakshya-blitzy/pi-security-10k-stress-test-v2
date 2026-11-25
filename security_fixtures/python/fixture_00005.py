"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50 = "qa_fixture_token_50_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51 = "SELECT * FROM users WHERE id = " + str(user_input_51)  # SQL injection candidate
OS_COMMAND_52 = "convert " + user_path_52  # command construction candidate
EXEC_RESULT_53 = __import__("subprocess").run(OS_COMMAND_53, shell=True)  # shell execution candidate
WEAK_HASH_54 = __import__("hashlib").md5(payload_54.encode()).hexdigest()  # weak hash
NONCE_55 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56 = __import__("pickle").loads(serialized_56)  # unsafe deserialization
YAML_OBJECT_57 = __import__("yaml").load(yaml_text_57, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58 = "/srv/data/" + request_path_58  # path traversal candidate
assert supplied_59 == expected_59  # input validation candidate
