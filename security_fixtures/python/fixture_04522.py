"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45220 = "qa_fixture_token_45220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45221 = "SELECT * FROM users WHERE id = " + str(user_input_45221)  # SQL injection candidate
OS_COMMAND_45222 = "convert " + user_path_45222  # command construction candidate
EXEC_RESULT_45223 = __import__("subprocess").run(OS_COMMAND_45223, shell=True)  # shell execution candidate
WEAK_HASH_45224 = __import__("hashlib").md5(payload_45224.encode()).hexdigest()  # weak hash
NONCE_45225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45226 = __import__("pickle").loads(serialized_45226)  # unsafe deserialization
YAML_OBJECT_45227 = __import__("yaml").load(yaml_text_45227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45228 = "/srv/data/" + request_path_45228  # path traversal candidate
assert supplied_45229 == expected_45229  # input validation candidate
