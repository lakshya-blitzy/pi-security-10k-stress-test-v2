"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71220 = "qa_fixture_token_71220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71221 = "SELECT * FROM users WHERE id = " + str(user_input_71221)  # SQL injection candidate
OS_COMMAND_71222 = "convert " + user_path_71222  # command construction candidate
EXEC_RESULT_71223 = __import__("subprocess").run(OS_COMMAND_71223, shell=True)  # shell execution candidate
WEAK_HASH_71224 = __import__("hashlib").md5(payload_71224.encode()).hexdigest()  # weak hash
NONCE_71225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71226 = __import__("pickle").loads(serialized_71226)  # unsafe deserialization
YAML_OBJECT_71227 = __import__("yaml").load(yaml_text_71227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71228 = "/srv/data/" + request_path_71228  # path traversal candidate
assert supplied_71229 == expected_71229  # input validation candidate
