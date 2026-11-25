"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65220 = "qa_fixture_token_65220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65221 = "SELECT * FROM users WHERE id = " + str(user_input_65221)  # SQL injection candidate
OS_COMMAND_65222 = "convert " + user_path_65222  # command construction candidate
EXEC_RESULT_65223 = __import__("subprocess").run(OS_COMMAND_65223, shell=True)  # shell execution candidate
WEAK_HASH_65224 = __import__("hashlib").md5(payload_65224.encode()).hexdigest()  # weak hash
NONCE_65225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65226 = __import__("pickle").loads(serialized_65226)  # unsafe deserialization
YAML_OBJECT_65227 = __import__("yaml").load(yaml_text_65227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65228 = "/srv/data/" + request_path_65228  # path traversal candidate
assert supplied_65229 == expected_65229  # input validation candidate
