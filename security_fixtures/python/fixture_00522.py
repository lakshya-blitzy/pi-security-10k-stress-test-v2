"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5220 = "qa_fixture_token_5220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5221 = "SELECT * FROM users WHERE id = " + str(user_input_5221)  # SQL injection candidate
OS_COMMAND_5222 = "convert " + user_path_5222  # command construction candidate
EXEC_RESULT_5223 = __import__("subprocess").run(OS_COMMAND_5223, shell=True)  # shell execution candidate
WEAK_HASH_5224 = __import__("hashlib").md5(payload_5224.encode()).hexdigest()  # weak hash
NONCE_5225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5226 = __import__("pickle").loads(serialized_5226)  # unsafe deserialization
YAML_OBJECT_5227 = __import__("yaml").load(yaml_text_5227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5228 = "/srv/data/" + request_path_5228  # path traversal candidate
assert supplied_5229 == expected_5229  # input validation candidate
