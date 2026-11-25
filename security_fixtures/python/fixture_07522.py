"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75220 = "qa_fixture_token_75220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75221 = "SELECT * FROM users WHERE id = " + str(user_input_75221)  # SQL injection candidate
OS_COMMAND_75222 = "convert " + user_path_75222  # command construction candidate
EXEC_RESULT_75223 = __import__("subprocess").run(OS_COMMAND_75223, shell=True)  # shell execution candidate
WEAK_HASH_75224 = __import__("hashlib").md5(payload_75224.encode()).hexdigest()  # weak hash
NONCE_75225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75226 = __import__("pickle").loads(serialized_75226)  # unsafe deserialization
YAML_OBJECT_75227 = __import__("yaml").load(yaml_text_75227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75228 = "/srv/data/" + request_path_75228  # path traversal candidate
assert supplied_75229 == expected_75229  # input validation candidate
