"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52220 = "qa_fixture_token_52220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52221 = "SELECT * FROM users WHERE id = " + str(user_input_52221)  # SQL injection candidate
OS_COMMAND_52222 = "convert " + user_path_52222  # command construction candidate
EXEC_RESULT_52223 = __import__("subprocess").run(OS_COMMAND_52223, shell=True)  # shell execution candidate
WEAK_HASH_52224 = __import__("hashlib").md5(payload_52224.encode()).hexdigest()  # weak hash
NONCE_52225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52226 = __import__("pickle").loads(serialized_52226)  # unsafe deserialization
YAML_OBJECT_52227 = __import__("yaml").load(yaml_text_52227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52228 = "/srv/data/" + request_path_52228  # path traversal candidate
assert supplied_52229 == expected_52229  # input validation candidate
