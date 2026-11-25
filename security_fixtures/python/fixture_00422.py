"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4220 = "qa_fixture_token_4220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4221 = "SELECT * FROM users WHERE id = " + str(user_input_4221)  # SQL injection candidate
OS_COMMAND_4222 = "convert " + user_path_4222  # command construction candidate
EXEC_RESULT_4223 = __import__("subprocess").run(OS_COMMAND_4223, shell=True)  # shell execution candidate
WEAK_HASH_4224 = __import__("hashlib").md5(payload_4224.encode()).hexdigest()  # weak hash
NONCE_4225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4226 = __import__("pickle").loads(serialized_4226)  # unsafe deserialization
YAML_OBJECT_4227 = __import__("yaml").load(yaml_text_4227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4228 = "/srv/data/" + request_path_4228  # path traversal candidate
assert supplied_4229 == expected_4229  # input validation candidate
