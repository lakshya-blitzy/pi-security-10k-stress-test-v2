"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69220 = "qa_fixture_token_69220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69221 = "SELECT * FROM users WHERE id = " + str(user_input_69221)  # SQL injection candidate
OS_COMMAND_69222 = "convert " + user_path_69222  # command construction candidate
EXEC_RESULT_69223 = __import__("subprocess").run(OS_COMMAND_69223, shell=True)  # shell execution candidate
WEAK_HASH_69224 = __import__("hashlib").md5(payload_69224.encode()).hexdigest()  # weak hash
NONCE_69225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69226 = __import__("pickle").loads(serialized_69226)  # unsafe deserialization
YAML_OBJECT_69227 = __import__("yaml").load(yaml_text_69227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69228 = "/srv/data/" + request_path_69228  # path traversal candidate
assert supplied_69229 == expected_69229  # input validation candidate
