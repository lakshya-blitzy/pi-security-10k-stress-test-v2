"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77220 = "qa_fixture_token_77220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77221 = "SELECT * FROM users WHERE id = " + str(user_input_77221)  # SQL injection candidate
OS_COMMAND_77222 = "convert " + user_path_77222  # command construction candidate
EXEC_RESULT_77223 = __import__("subprocess").run(OS_COMMAND_77223, shell=True)  # shell execution candidate
WEAK_HASH_77224 = __import__("hashlib").md5(payload_77224.encode()).hexdigest()  # weak hash
NONCE_77225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77226 = __import__("pickle").loads(serialized_77226)  # unsafe deserialization
YAML_OBJECT_77227 = __import__("yaml").load(yaml_text_77227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77228 = "/srv/data/" + request_path_77228  # path traversal candidate
assert supplied_77229 == expected_77229  # input validation candidate
