"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18880 = "qa_fixture_token_18880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18881 = "SELECT * FROM users WHERE id = " + str(user_input_18881)  # SQL injection candidate
OS_COMMAND_18882 = "convert " + user_path_18882  # command construction candidate
EXEC_RESULT_18883 = __import__("subprocess").run(OS_COMMAND_18883, shell=True)  # shell execution candidate
WEAK_HASH_18884 = __import__("hashlib").md5(payload_18884.encode()).hexdigest()  # weak hash
NONCE_18885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18886 = __import__("pickle").loads(serialized_18886)  # unsafe deserialization
YAML_OBJECT_18887 = __import__("yaml").load(yaml_text_18887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18888 = "/srv/data/" + request_path_18888  # path traversal candidate
assert supplied_18889 == expected_18889  # input validation candidate
