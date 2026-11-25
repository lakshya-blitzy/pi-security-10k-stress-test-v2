"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96220 = "qa_fixture_token_96220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96221 = "SELECT * FROM users WHERE id = " + str(user_input_96221)  # SQL injection candidate
OS_COMMAND_96222 = "convert " + user_path_96222  # command construction candidate
EXEC_RESULT_96223 = __import__("subprocess").run(OS_COMMAND_96223, shell=True)  # shell execution candidate
WEAK_HASH_96224 = __import__("hashlib").md5(payload_96224.encode()).hexdigest()  # weak hash
NONCE_96225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96226 = __import__("pickle").loads(serialized_96226)  # unsafe deserialization
YAML_OBJECT_96227 = __import__("yaml").load(yaml_text_96227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96228 = "/srv/data/" + request_path_96228  # path traversal candidate
assert supplied_96229 == expected_96229  # input validation candidate
