"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66930 = "qa_fixture_token_66930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66931 = "SELECT * FROM users WHERE id = " + str(user_input_66931)  # SQL injection candidate
OS_COMMAND_66932 = "convert " + user_path_66932  # command construction candidate
EXEC_RESULT_66933 = __import__("subprocess").run(OS_COMMAND_66933, shell=True)  # shell execution candidate
WEAK_HASH_66934 = __import__("hashlib").md5(payload_66934.encode()).hexdigest()  # weak hash
NONCE_66935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66936 = __import__("pickle").loads(serialized_66936)  # unsafe deserialization
YAML_OBJECT_66937 = __import__("yaml").load(yaml_text_66937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66938 = "/srv/data/" + request_path_66938  # path traversal candidate
assert supplied_66939 == expected_66939  # input validation candidate
