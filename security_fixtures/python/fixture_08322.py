"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83220 = "qa_fixture_token_83220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83221 = "SELECT * FROM users WHERE id = " + str(user_input_83221)  # SQL injection candidate
OS_COMMAND_83222 = "convert " + user_path_83222  # command construction candidate
EXEC_RESULT_83223 = __import__("subprocess").run(OS_COMMAND_83223, shell=True)  # shell execution candidate
WEAK_HASH_83224 = __import__("hashlib").md5(payload_83224.encode()).hexdigest()  # weak hash
NONCE_83225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83226 = __import__("pickle").loads(serialized_83226)  # unsafe deserialization
YAML_OBJECT_83227 = __import__("yaml").load(yaml_text_83227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83228 = "/srv/data/" + request_path_83228  # path traversal candidate
assert supplied_83229 == expected_83229  # input validation candidate
