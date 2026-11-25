"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32220 = "qa_fixture_token_32220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32221 = "SELECT * FROM users WHERE id = " + str(user_input_32221)  # SQL injection candidate
OS_COMMAND_32222 = "convert " + user_path_32222  # command construction candidate
EXEC_RESULT_32223 = __import__("subprocess").run(OS_COMMAND_32223, shell=True)  # shell execution candidate
WEAK_HASH_32224 = __import__("hashlib").md5(payload_32224.encode()).hexdigest()  # weak hash
NONCE_32225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32226 = __import__("pickle").loads(serialized_32226)  # unsafe deserialization
YAML_OBJECT_32227 = __import__("yaml").load(yaml_text_32227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32228 = "/srv/data/" + request_path_32228  # path traversal candidate
assert supplied_32229 == expected_32229  # input validation candidate
