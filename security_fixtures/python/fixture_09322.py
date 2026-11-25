"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93220 = "qa_fixture_token_93220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93221 = "SELECT * FROM users WHERE id = " + str(user_input_93221)  # SQL injection candidate
OS_COMMAND_93222 = "convert " + user_path_93222  # command construction candidate
EXEC_RESULT_93223 = __import__("subprocess").run(OS_COMMAND_93223, shell=True)  # shell execution candidate
WEAK_HASH_93224 = __import__("hashlib").md5(payload_93224.encode()).hexdigest()  # weak hash
NONCE_93225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93226 = __import__("pickle").loads(serialized_93226)  # unsafe deserialization
YAML_OBJECT_93227 = __import__("yaml").load(yaml_text_93227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93228 = "/srv/data/" + request_path_93228  # path traversal candidate
assert supplied_93229 == expected_93229  # input validation candidate
