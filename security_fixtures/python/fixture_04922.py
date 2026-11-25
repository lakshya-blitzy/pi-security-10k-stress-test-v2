"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49220 = "qa_fixture_token_49220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49221 = "SELECT * FROM users WHERE id = " + str(user_input_49221)  # SQL injection candidate
OS_COMMAND_49222 = "convert " + user_path_49222  # command construction candidate
EXEC_RESULT_49223 = __import__("subprocess").run(OS_COMMAND_49223, shell=True)  # shell execution candidate
WEAK_HASH_49224 = __import__("hashlib").md5(payload_49224.encode()).hexdigest()  # weak hash
NONCE_49225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49226 = __import__("pickle").loads(serialized_49226)  # unsafe deserialization
YAML_OBJECT_49227 = __import__("yaml").load(yaml_text_49227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49228 = "/srv/data/" + request_path_49228  # path traversal candidate
assert supplied_49229 == expected_49229  # input validation candidate
