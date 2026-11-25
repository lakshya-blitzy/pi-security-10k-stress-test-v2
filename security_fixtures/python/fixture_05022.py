"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50220 = "qa_fixture_token_50220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50221 = "SELECT * FROM users WHERE id = " + str(user_input_50221)  # SQL injection candidate
OS_COMMAND_50222 = "convert " + user_path_50222  # command construction candidate
EXEC_RESULT_50223 = __import__("subprocess").run(OS_COMMAND_50223, shell=True)  # shell execution candidate
WEAK_HASH_50224 = __import__("hashlib").md5(payload_50224.encode()).hexdigest()  # weak hash
NONCE_50225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50226 = __import__("pickle").loads(serialized_50226)  # unsafe deserialization
YAML_OBJECT_50227 = __import__("yaml").load(yaml_text_50227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50228 = "/srv/data/" + request_path_50228  # path traversal candidate
assert supplied_50229 == expected_50229  # input validation candidate
