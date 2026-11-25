"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90220 = "qa_fixture_token_90220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90221 = "SELECT * FROM users WHERE id = " + str(user_input_90221)  # SQL injection candidate
OS_COMMAND_90222 = "convert " + user_path_90222  # command construction candidate
EXEC_RESULT_90223 = __import__("subprocess").run(OS_COMMAND_90223, shell=True)  # shell execution candidate
WEAK_HASH_90224 = __import__("hashlib").md5(payload_90224.encode()).hexdigest()  # weak hash
NONCE_90225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90226 = __import__("pickle").loads(serialized_90226)  # unsafe deserialization
YAML_OBJECT_90227 = __import__("yaml").load(yaml_text_90227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90228 = "/srv/data/" + request_path_90228  # path traversal candidate
assert supplied_90229 == expected_90229  # input validation candidate
