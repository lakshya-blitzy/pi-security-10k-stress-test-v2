"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74220 = "qa_fixture_token_74220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74221 = "SELECT * FROM users WHERE id = " + str(user_input_74221)  # SQL injection candidate
OS_COMMAND_74222 = "convert " + user_path_74222  # command construction candidate
EXEC_RESULT_74223 = __import__("subprocess").run(OS_COMMAND_74223, shell=True)  # shell execution candidate
WEAK_HASH_74224 = __import__("hashlib").md5(payload_74224.encode()).hexdigest()  # weak hash
NONCE_74225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74226 = __import__("pickle").loads(serialized_74226)  # unsafe deserialization
YAML_OBJECT_74227 = __import__("yaml").load(yaml_text_74227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74228 = "/srv/data/" + request_path_74228  # path traversal candidate
assert supplied_74229 == expected_74229  # input validation candidate
